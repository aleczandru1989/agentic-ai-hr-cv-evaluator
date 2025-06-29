import gradio as gr


class Tools:

    @staticmethod
    def get():
        return [
            {"type": "function", "function": Tools.seniority_mismatch_json()},
            {"type": "function", "function": Tools.skills_mismatch_json()},
            {"type": "function", "function": Tools.candidate_match_json()}
        ]
    
    
    @staticmethod
    def seniority_mismatch_json():
        return {
            "name": "seniority_mismatch",
            "description": "Use this tool when there is a seniority mismatch",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "The email address of this user"
                    },
                    "candidate_name": {
                        "type": "string",
                        "description": "The user's name, if they provided it"
                    }
                },
                "required": ["candidate_name", "email"],
                "additionalProperties": False
            }
        }

    @staticmethod
    def seniority_mismatch(candidate_name, email):
        msg = f"⚠️ {candidate_name} with contact {email} does not match on a seniority level"
        print(msg)
        return msg

    @staticmethod
    def skills_mismatch_json():
        return {
            "name": "skills_mismatch",
            "description": "Use this tool when there is a seniority mismatch",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "The email address of this user"
                    },
                    "candidate_name": {
                        "type": "string",
                        "description": "The user's name, if they provided it"
                    }
                },
                "required": ["candidate_name", "email"],
                "additionalProperties": False
            }
        }
    @staticmethod
    def skills_mismatch(candidate_name, email):
        msg = f"⚠️ {candidate_name} with contact {email} does not match on a skills level"
        print(msg)
        return msg

    @staticmethod
    def candidate_match_json():
        return {
            "name": "candidate_match",
            "description": "Use this tool when there is a seniority mismatch",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "The email address of this user"
                    },
                    "candidate_name": {
                        "type": "string",
                        "description": "The user's name, if they provided it"
                    }
                },
                "required": ["candidate_name", "email"],
                "additionalProperties": False
            }
        }

    @staticmethod
    def candidate_match(candidate_name, email):
        msg = f"✅ {candidate_name} with contact {email} is the perfect candidate"
        print(msg)
        return msg

    @staticmethod
    def call_tool_by_name(name, **kwargs):
        """
        Call a tool method by its name with the given arguments.
        Example: Tools.call_tool_by_name('seniority_mismatch', candidate_name='John', email='john@example.com')
        """
        tool_map = {
            'seniority_mismatch': Tools.seniority_mismatch,
            'skills_mismatch': Tools.skills_mismatch,
            'candidate_match': Tools.candidate_match,
        }
        tool_func = tool_map.get(name)
        if tool_func is None:
            raise ValueError(f"Tool '{name}' not found.")
        
        return tool_func(**kwargs)
