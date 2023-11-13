

from database import sync_engine, recreate_table_list
from user.models import User

if __name__ == '__main__':
    recreate_table_list([User], sync_engine)
