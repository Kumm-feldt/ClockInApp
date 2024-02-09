from flask import Flask, render_template, request, url_for, redirect
import sqlite3
from sqlite3 import Error

company = input("Company Name")


class Employee:
    def __init__(self, name, lastname, email, phone_number):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone_number = phone_number


class Employer:
    def __init__(self, name, lastname, email, phone_number, job):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone_number = phone_number
        self.job = {
            "place":job.place,
            "position":job.position,
            "building":job.building,
        }


