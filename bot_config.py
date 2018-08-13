import configparser


class BotConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./setting.conf', encoding="utf-8_sig")
        self.bot_token = self.config['default']['bot_token']
        self.channel_ids = self.config['default']['channel_id'].split()
        self.special_channel_ids = self.config['default']['special_channel_id'].split()
        self.all_channel_ids = []
        self.all_channel_ids.extend(self.channel_ids)
        self.all_channel_ids.extend(self.special_channel_ids)
        self.command_help = self.config['default']['command_help']
        self.command_tier = self.config['default']['command_tier']
        self.command_ship = self.config['default']['command_ship']
        self.command_choice = self.config['default']['command_choice']
        self.command_pickup = self.config['default']['command_pickup']
        self.command_team = self.config['default']['command_team']
        self.command_luck = self.config['default']['command_luck']
        self.command_kuji = self.config['default']['command_kuji']
        self.command_enter = self.config['default']['command_enter']
        self.command_leave = self.config['default']['command_leave']
        self.release_commands = [self.command_help,
                                 self.command_tier,
                                 self.command_ship,
                                 self.command_choice,
                                 self.command_pickup,
                                 self.command_team,
                                 self.command_luck]
        self.commands = list(self.release_commands)
        self.commands.append(self.command_kuji)
        self.commands.append(self.command_enter)
        self.commands.append(self.command_leave)
