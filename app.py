import streamlit as st
import pandas as pd
import autogen

# Initialize session state
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "agents_config" not in st.session_state:
    st.session_state.agents_config = pd.DataFrame(
        columns=[
            "Name",
            "Model",
            "System Message",
            "Temperature",
            "Description",
        ]
    )
if "messages" not in st.session_state:
    st.session_state.messages = []

st.set_page_config(layout="wide")
st.title("AutoGen Multi-Agent Group Chat")

# Sidebar - API Key
with st.sidebar:
    st.session_state.api_key = st.text_input(
        "OpenRouter API Key", value=st.session_state.api_key, type="password"
    )

# Tab 1: Configure Agents
tab1, tab2 = st.tabs(["Configure Agents", "Run Group Chat"])

with tab1:
    st.subheader("Agent Configuration")

    col1, col2 = st.columns(2)
    with col1:
        agent_name = st.text_input("Agent Name")
        model = st.text_input("Model Name (e.g., meta-llama/llama-2-7b)")
        system_msg = st.text_area("System Message")

    with col2:
        temperature = st.slider("Temperature", 0.0, 2.0, 0.7)
        description = st.text_area("Agent Description")

    if st.button("Add Agent"):
        new_agent = pd.DataFrame(
            [
                {
                    "Name": agent_name,
                    "Model": model,
                    "System Message": system_msg,
                    "Temperature": temperature,
                    "Description": description,
                }
            ]
        )
        st.session_state.agents_config = pd.concat(
            [st.session_state.agents_config, new_agent], ignore_index=True
        )
        st.success("Agent added!")

    st.subheader("Configured Agents")
    edited_df = st.data_editor(st.session_state.agents_config, use_container_width=True)
    st.session_state.agents_config = edited_df

    if st.button("Download Agents Config"):
        csv = st.session_state.agents_config.to_csv(index=False)
        st.download_button(
            "Download CSV", csv, "agents_config.csv", "text/csv"
        )

with tab2:
    st.subheader("Run Group Chat")

    if len(st.session_state.agents_config) < 2:
        st.error("Configure at least 2 agents first!")
    else:
        initial_message = st.text_area("Initial Message")
        max_rounds = st.number_input("Max Rounds", value=10, min_value=1)

        if st.button("Start Group Chat"):
            if not st.session_state.api_key:
                st.error("Please enter API Key!")
            elif not initial_message:
                st.error("Please enter initial message!")
            else:
                st.session_state.messages = []

                # Configure LLM
                config_list = [
                    {
                        "model": row["Model"],
                        "api_key": st.session_state.api_key,
                        "base_url": "https://openrouter.ai/api/v1",
                    }
                    for _, row in st.session_state.agents_config.iterrows()
                ]

                llm_config = {
                    "cache_seed": 42,
                    "temperature": st.session_state.agents_config.iloc[
                        0
                    ]["Temperature"],
                    "config_list": config_list,
                    "timeout": 120,
                }

                # Create user proxy (initiator)
                user_proxy = autogen.UserProxyAgent(
                    name="Admin",
                    system_message="A human admin. Interact with the group to oversee the conversation.",
                    human_input_mode="NEVER",
                    code_execution_config=False,
                )

                # Create assistant agents from config
                agents = [user_proxy]
                for _, row in st.session_state.agents_config.iterrows():
                    agent = autogen.AssistantAgent(
                        name=row["Name"],
                        system_message=row["System Message"],
                        llm_config=llm_config,
                    )
                    agents.append(agent)

                # Create group chat
                groupchat = autogen.GroupChat(
                    agents=agents,
                    messages=[],
                    max_round=int(max_rounds),
                )

                # Create manager
                manager = autogen.GroupChatManager(
                    groupchat=groupchat, llm_config=llm_config
                )

                status = st.status("Running group chat...", expanded=True)

                try:
                    # Initiate chat
                    user_proxy.initiate_chat(manager, message=initial_message)

                    # Extract messages from groupchat
                    for msg in groupchat.messages:
                        agent_name = msg.get("name", "Unknown")
                        content = msg.get("content", "")
                        st.session_state.messages.append(
                            {
                                "Agent": agent_name,
                                "Message": content,
                            }
                        )
                        status.write(f"**{agent_name}:** {content[:100]}...")

                    status.update(label="Group chat completed!", state="complete")
                    st.success("Group chat completed!")

                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    status.update(label=f"Error: {str(e)}", state="error")

        if st.session_state.messages:
            st.subheader("Conversation")
            with st.expander("View Messages", expanded=True):
                for msg in st.session_state.messages:
                    st.write(f"**{msg['Agent']}:** {msg['Message']}")

            csv = pd.DataFrame(st.session_state.messages).to_csv(index=False)
            st.download_button(
                "Download Messages", csv, "conversation.csv", "text/csv"
            )