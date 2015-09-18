
from killranswers.categories.models import Category
from killranswers.connections import cassandra

def create_sample_tree():
    # creates a tree 5 levels deep for testing
    # 5 categories per level
    pass

# creating a root category
def test_create_root():
    root = Category.create_root("test")

# creating new categories
def test_create_category():
    pass


# moving categories
def test_move_category_children_parents_updated():
    pass

def test_move_category_parents_updated():
    pass

def test_move_category_stats_updated():
    pass
