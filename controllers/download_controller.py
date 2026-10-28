from flask import jsonify, send_from_directory

UPLOAD_FOLDER = 'UPLOADS'

class DownloadController:

    @staticmethod
    def download_file(filename):
        try:
            return send_from_directory(UPLOAD_FOLDER, as_attacchment=true)
            except FileNotFoundError:
                return jsonify({"error": "Arquivo não encontrado"}), 404

