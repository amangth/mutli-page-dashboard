import dash
import dash_auth


USER_PASSWORDS_MAP = {
    "username1": "user1"
}


app = dash.Dash(__name__)
app.config['suppress_callback_exceptions'] = True

auth = dash_auth.BasicAuth(app,USER_PASSWORDS_MAP)
server = app.server