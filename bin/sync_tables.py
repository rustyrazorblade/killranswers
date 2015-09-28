#!/usr/bin/env python
import sys
sys.path.append("")

from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import ModelMetaClass
from killranswers.connections import  cassandra

from killranswers.categories.models import *
from killranswers.questions.models import *
from killranswers.users.models import *
from killranswers.answers.models import *

cassandra()

for model in [x for x in globals().values()
                if isinstance(x, ModelMetaClass) and
                x.__abstract__ == False]:
    # import ipdb; ipdb.set_trace()

    sync_table(model)

Category.create_root()
