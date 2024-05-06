from datetime import date

import logfire

logfire.info("Hello, {name}!", name="world")

with logfire.span("Asking the user their {question}", question="age"):
    user_input = input("How old are you [YYYY-mm-dd]? ")
    dob = date.fromisoformat(user_input)
    logfire.debug("{dob=} {age=!r}", dob=dob, age=date.today() - dob)
