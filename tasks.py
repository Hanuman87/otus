from invoke import task

@task
def setup(ctx):
    ctx.run("uv sync", pty=True)
    ctx.run("uv python install 3.11.12", pty=True)