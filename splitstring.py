class SplitString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING",),
            }
        }

    RETURN_TYPES = ("STRING",) * 12
    FUNCTION = "split_string"

    def split_string(self, string: str):
        return (*string.split("\n\n")[:12],)
