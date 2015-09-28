from uuid import uuid4, uuid1
from killranswers.categories.models import Category, root
from killranswers.connections import cassandra

cassandra()

def create_sample_tree():
    # creates a tree 5 levels deep for testing
    # 5 categories per level
    pass

# creating a root category
def test_create_root():
    root = Category.create_root()
    cat = Category.get_root()
    assert cat.name == "root"

# creating new categories
def test_create_category():
    r = Category.get(category_id=root)
    cat = r.create_sub("something")
    assert cat is not None
    assert len(cat.parent_categories) == 0
    sub = cat.create_sub("subcat")
    assert len(sub.parent_categories) == 1

def test_get_children():
    r = Category.get(category_id=root)
    # fake root
    froot = r.create_sub("something")
    cat1 = froot.create_sub("sub1")
    cat2 = froot.create_sub("sub1")
    children = froot.get_children()
    assert len(children) == 2


# moving categories
def test_move_category_children_parents_updated():
    pass

def test_move_category_parents_updated():
    pass

def test_move_category_stats_updated():
    pass
