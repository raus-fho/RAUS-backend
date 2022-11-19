from app.api.db import models
from .db import SessionLocal, engine
from flask import Flask, jsonify, request
from sqlalchemy.orm import scoped_session, sessionmaker
import json

app = Flask(__name__)

app.session = scoped_session(session_factory=sessionmaker(bind=engine))

def get_current_status():
    status = app.session.query(models.Status).first()
    return row2dict(status)

def update_status():
    status = jsonify(request.json).json 
    status.update({'actuator_status':status['actuator_status']})
    app.session.query(models.Status)\
        .update(status)
    app.session.commit()
    return status

def get_all_history():
    hists = app.session.query(models.History).all()
    history_list = []
    for hist in hists:
        history_list.append(row2dict(hist))
          
    return history_list

def save_history_to_db():
    hist = jsonify(request.json).json
    new_hist = models.History(
        humidity = hist['humidity'],
        actuator_status = hist['actuator_status']
    )
    app.session.add(new_hist)
    app.session.commit()
    
    return hist    
    
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d