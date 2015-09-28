from killranswers import Question, Category

root = Category.get_root()

def get_cat():
    # how to get those awesome scaffolds
    # TODO: use test name instead of the hard coded name
    return root.create_sub("category-test")


def test_ask():
    c = get_cat()

    q = Question.create(c, "test question")
