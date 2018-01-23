from ftfy.fixes import (
    fix_encoding, fix_encoding_and_explain, apply_plan, possible_encoding,
    remove_control_chars, fix_surrogates
)
from ftfy import fix_text, fix_text_segment

import unicodedata
import sys

class Arquivo(object):

    def __init__(self, var):
        #getting data
        self.id = fix_text(var['id'])
        self.name = fix_text(var['name'])
        self.mimeType = fix_text(var['mimeType'])
        self.version = fix_text(var['version'])
        self.parents = (list(var['parents']))
        self.isFolder = False
        self.isGDFile = False
        self.GDFileType = -1
        self.query = var
            
        #nem todo arquivo tem extensão e tamanho (se for arquivo gdrive)
        if(var.has_key("size")):
            self.size = fix_text(var['size'])
        else:
            self.size = "none"
        if(var.has_key("fileExtension")):
            self.fileExtension = fix_text(var['fileExtension'])
        else:
            self.fileExtension = "none"

        #0 .document
        #1 .spreadsheet
        #2 .form
        #3 .presentation
        #text/csv
        if (".document" in self.mimeType):
            self.GDFileType = 0
        elif (".spreadsheet" in self.mimeType):
            self.GDFileType = 1
        elif (".form" in self.mimeType):
            self.GDFileType = 2
        elif (".presentation" in self.mimeType):
            self.GDFileType = 3
    
        if(".folder" in self.mimeType):
            self.isFolder = True
        else:
            self.isFolder = False

        if(self.size=="none" and self.fileExtension=="none"):
            self.isGDFile = True
        else:
            self.isGDFile = False

    def format_str(self, content):
        return content.encode(sys.stdout.encoding, errors="replace")

    def __str__(self):
        b = ""
        for i, s in enumerate(self.parents):
            b = b + (self.parents[i]).encode("utf-8") + ", "

        b = b[:-2]#remover ultima virgula e espaço
        
        #a = "id: " + (self.id).encode("utf-8") + "\n"
        #a = a + "name: " + (self.name).encode("utf-8") + "\n"
        #a = "id: " + (self.id) + "\n"
        #a = a + "name: " + (self.name) + "\n"
        a = "id: " + self.format_str(self.id) + "\n"
        a = a + "name: " + self.format_str(self.name) + "\n"
        a = a + "mimeType: " + str(self.mimeType) + "\n"
        a = a + "version: " + str(self.version) + "\n"
        a = a + "fileExtension: " + str(self.fileExtension) + "\n"
        a = a + "size: " + str(self.size) + "\n"
        a = a + "isFolder: " + str(self.isFolder) + "\n"
        a = a + "isGDFile: " + str(self.isGDFile) + "\n"
        a = a + "GDFileType: " + str(self.GDFileType) + "\n"
        a = a + "parents: " + b + "\n"
        a = a + "ENTIRELY QUERY: " + str(self.query) + "\n"
        return a
