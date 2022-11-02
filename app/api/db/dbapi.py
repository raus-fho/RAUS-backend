from app.api.db import models
from .db import SessionLocal, engine
from flask import Flask, _app_ctx_stack, jsonify, url_for
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.session = scoped_session(session_factory=sessionmaker(bind=engine))

def get_current_status():
    status = app.session.query(models.Status).first()
    return row2dict(status)

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d