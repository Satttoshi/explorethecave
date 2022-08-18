from appconf import conf


def is_channel_allowed(ctx) -> bool:
    return ctx.channel.id == conf.command_channel
