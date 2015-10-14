# -*- coding: utf-8 -*-
__author__ = 'jinming'


from extensions import db


class Endpoint(db.Model):
    """
    This model stores the information of endpoint for the app and mobile device.
    ===============
    For IOS endpoint:
    device_type: IOS=0
    device_token: the token get from apple.
    endpoint_arn: the amazon resouce name of the endpoint, this arn get from amazon.
    ===============
    For IOS endpoint:
    device_type: ANDROID=1
    device_token: the token get from baidu.
    endpoint_arn: the amazon resouce name of the endpoint, this arn get from amazon.
    """
    __tablename__ = 'endpoint'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    device_type = db.Column(db.Integer)
    device_token = db.Column(db.String(100), unique=True)
    endpoint_arn = db.Column(db.String(200), unique=True)
    is_active = db.Column(db.Boolean())
    date_added = db.Column(db.DateTime())

    topic_endpoints = db.relationship('TopicEndpoint', backref='endpoint', lazy='dynamic')




class Topic(db.Model):
    """
    This model stores all topics in system. One topic is one group,
    you can put any endpoint you want to a topic, then these endpoints
    are in the group.
    """
    __tablename__ = 'topic'

    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(20))
    topic_lang = db.Column(db.String(20))
    topic_arn = db.Column(db.String(200), unique=True)
    is_active = db.Column(db.Boolean)
    date_added = db.Column(db.DateTime)




class TopicEndpoint(db.Model):
    """
    This model stores the detail information of subscribed topic of every endpoint,
    one endpoint maybe in several topics.
    """
    __tablename__ = 'topic_endpoint'

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    endpoint_id = db.Column(db.Integer, db.ForeignKey('endpoint.id'))
    subscribe_arn = db.Column(db.String(200), unique=True)
    is_active = db.Column(db.Boolean)
    date_added = db.Column(db.DateTime)



















