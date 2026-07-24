# Security-hardened plugin loader.
# Only reviewed music and administration modules are loaded at startup.
ALL_MODULES = ['.admins.auth', '.admins.callback', '.admins.loop', '.admins.pause', '.admins.resume', '.admins.seek', '.admins.shuffle', '.admins.skip', '.admins.speed', '.admins.stop', '.bot.help', '.bot.repo', '.bot.settings', '.bot.start', '.play.channel', '.play.live', '.play.play', '.play.playmode', '.sudo.autoend', '.sudo.blchat', '.sudo.block', '.sudo.gban', '.sudo.logger', '.sudo.maintenance', '.sudo.sudoers', '.tools.active', '.tools.language', '.tools.ping', '.tools.queue', '.tools.song', '.tools.stats', '.misc.autoleave', '.misc.broadcast', '.misc.info', '.misc.state']
__all__ = ALL_MODULES + ["ALL_MODULES"]
