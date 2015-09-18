#!/usr/bin/env python
import sys
sys.path.append("")

from cassandra.cqlengine.management import sync_table
from killranswers.connections import  cassandra
from killranswers.categories.models import *

cassandra()

sync_table(Category)
Category.create_root()
