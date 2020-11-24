# Maggie Cloos
# Agile UNO Module 9
# 11/23/2020

from my_module import greeting


def test_greeting_pass():
    assert my_module.greeting("Maggie") == "Hello Maggie" , "test passed"

def test_greeting_fail():
    assert my_module.greeting("") != "Hello Maggie", "test failed"

def test_letter_text_pass():
    assert my_module.letter_text(name="Maggie", amount="10", denomination="dollars") == \
        "Hello Maggie, this letter is to inform you that you have won 10 dollars", "test failed"

def test_letter_text_fail():
    assert my_module.letter_text(name="Maggie", amount="10") != \
        "Hello Maggie, this letter is to inform you that you have won 10 dollars.", "test failed"

