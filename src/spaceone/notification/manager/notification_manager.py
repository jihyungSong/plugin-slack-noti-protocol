from spaceone.core.manager import BaseManager
from spaceone.notification.connector.slack import SlackConnector


class NotificationManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = None

    def set_connector(self, token):
        self.conn: SlackConnector = self.locator.get_connector('SlackConnector', token=token)

    def dispatch(self, slack_channel, message):
        self.conn.chat_message(slack_channel, message)

