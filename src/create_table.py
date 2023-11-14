

from database import recreate_table_list, sync_engine
from user.models import User

if __name__ == '__main__':
    recreate_table_list([User], sync_engine)
