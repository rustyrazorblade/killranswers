from uuid import uuid1, uuid4
import uuid
import copy
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *

root = uuid.UUID("00000000-0000-0000-0000-000000000000")

class Category(Model):
    __table_name__ = "category"
    category_id = UUID(primary_key=True, default=uuid4)
    name = Text()
    parent_categories = List(UUID) # first parent on the left, root at the end

    def create_sub(self, name):
        # set up parent categories

        parents = self.parent_categories[:]
        if self.category_id != root:
            parents.insert(0, self.category_id)
        cat = Category.create(name=name, parent_categories=parents)
        # update the children table
        CategoryChildren.create(category_id=self.category_id,
                                child_category_id=cat.category_id,
                                child_category_name=cat.name)
        # update statistics
        return cat

    @classmethod
    def create_root(cls):
        # creating a root category has slightly different rules
        return super(cls, Category).create(category_id=root, name="root")

    @classmethod
    def get_root(cls):
        return super(cls, Category).get(category_id=root)

    @classmethod
    def get_top_levels(cls):
        pass

    @property
    def parent(self):
        # returns a single Category object or None
        if self.parent_categories:
            return Category.get(category_id=self.parent_categories[0])



    @property
    def parents(self):
        # returns a list of category objects
        result = []
        for x in self.parent_categories:
            result.append(Category.get(category_id=x))
        return result

    def get_children(self):
        return CategoryChildren.objects(category_id=self.category_id)

    # track the full category list
    def move(self, new_parent):
        """
        moves to a new parent category
        updates the category children
        updates the category counts
        """
        pass


class CategoryCounters(Model):
    category_id = UUID(primary_key=True)

    questions = Counter() # direct questions
    questions_total = Counter() # including all subs
    answers = Counter() # direct
    answers_total = Counter() # includes subs


class CategoryChildren(Model):
    """
    maintaining the list of children of a given category
    """
    category_id = UUID(primary_key=True)
    child_category_id = UUID(primary_key=True)
    child_category_name = Text()
