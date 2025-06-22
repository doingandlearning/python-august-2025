## Error Codes - ERR_PARTICIPATION_API_CALL

class BBCApiError(Exception):
    def __init__(self, message, error_code = "ERR_API_ERROR"):
        # self.message = message
        super().__init__(message)
        # A fully formed Exception
        self.error_code = error_code

    def print(self):
        print(self.message)


def third_party_library():
    raise BBCApiError("For some other reason", "ERR_BBC_NEWSROUND_STUDIO")

try:
    int("121")
    third_party_library()
except ValueError:  # is this our error we're handling or a 3rd party's?
    print("Whoops! Try a different number!")
except BBCApiError as exp:
    print("Call the team - tell them to fix their stuff!")
    print(f"{exp.error_code}")
    print(exp.message)