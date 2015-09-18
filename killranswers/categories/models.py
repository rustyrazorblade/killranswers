from uuid import uuid1

from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *

root = "00000000-0000-0000-0000-000000000000"

class Category(Model):
    category_id = UUID(primary_key=True, default=uuid1)
    name = Text()
    parent_categories = List(TimeUUID) # first parent on the left, root at the end
    # parent_category_id = TimeUUID(primary_key=True)


    @classmethod
    def create(self, parent, name):
        assert isinstance(parent, Category)
        # set up parent categories
        return super(self, Category).create(name=name)

    @classmethod
    def create_root(self):
        # creating a root category has slightly different rules
        return super(self, Category).create(category_id=root, name="root")

    @classmethod
    def get_top_levels(cls):
        pass

    @property
    def parent(self):
        # returns a single Category object or None
        pass

    @property
    def parents(self):
        # returns a list of category objects
        pass

    # track the full category list
    def move(self, new_parent):
        """
        moves to a new parent category
        updates the category children
        updates the category counts
        """
        pass


class CategoryCounters(Model):
    category_id = TimeUUID(primary_key=True)

    questions = Counter() # direct questions
    questions_total = Counter() # including all subs
    answers = Counter() # direct
    answers_total = Counter() # includes subs


class CategoryChildren(Model):
    """
    maintaining the list of children of a given category
    """
    category_id = TimeUUID(primary_key=True)
    child_category_id = TimeUUID(primary_key=True)
    child_category_name = Text()
