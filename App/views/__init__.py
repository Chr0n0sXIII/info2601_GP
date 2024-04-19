# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .home import home_views
from .play import play_views
from .signup import signup_views
from .leaderboard import leaderboard_views


views = [user_views, index_views, auth_views,home_views,play_views, signup_views, leaderboard_views] 
# blueprints must be added to this list