from flask import Flask, jsonify, request

from contact import (
    add_contact,
    create_table,
    delete_contact,
    list_contact,
    update_contact,
)

