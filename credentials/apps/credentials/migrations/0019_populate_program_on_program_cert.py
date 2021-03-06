# Generated by Django 2.2.17 on 2021-04-02 21:09

from django.db import migrations


def populate_program(apps, schema_editor):
    Program = apps.get_model("catalog", "Program")
    ProgramCertificate = apps.get_model("credentials", "ProgramCertificate")
    for program_cert in ProgramCertificate.objects.all():
        try:
            program = Program.objects.get(uuid=program_cert.program_uuid)
        except Program.DoesNotExist:
            continue
        program_cert.program = program
        program_cert.save()


class Migration(migrations.Migration):

    dependencies = [
        ("credentials", "0018_programcertificate_program"),
    ]

    operations = [migrations.RunPython(populate_program)]
