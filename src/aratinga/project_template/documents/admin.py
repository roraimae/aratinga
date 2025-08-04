from django.contrib import admin
from .models import CustomDocument
import os


class CustomDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "file_deleted")  # Colunas exibidas na lista de documentos

    def check_file_existence(self, document_id):
        try:
            # Obter o documento pelo ID
            document = CustomDocument.objects.get(id=document_id)

            # Verificar se o arquivo físico existe no sistema de arquivos
            file_path = document.file.path
            if os.path.exists(file_path):
                return True
            else:
                return False

        except CustomDocument.DoesNotExist:
            return False

    def file_deleted(self, obj):
        return self.check_file_existence(obj.id)  # Verifica se o arquivo foi excluído

    file_deleted.boolean = True  # Define como um valor booleano
    file_deleted.short_description = "File Exist"  # Título da coluna


admin.site.register(
    CustomDocument, CustomDocumentAdmin
)  # Registrar a classe de administração personalizada
