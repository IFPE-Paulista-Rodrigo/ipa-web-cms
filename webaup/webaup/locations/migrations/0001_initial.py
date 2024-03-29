# Generated by Django 4.1.6 on 2023-03-31 21:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("wagtailcore", "0078_referenceindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocationsIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "introduction",
                    models.TextField(
                        blank=True, help_text="Texto para descrever a página"
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Somente modo paisagem; largura horizontal entre 1000px and 3000px.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="LocationPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "introduction",
                    models.TextField(
                        blank=True, help_text="Texto para descrever a página"
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading_text",
                                            wagtail.blocks.CharBlock(
                                                form_classname="title", required=True
                                            ),
                                        ),
                                        (
                                            "size",
                                            wagtail.blocks.ChoiceBlock(
                                                blank=True,
                                                choices=[
                                                    ("", "Select a header size"),
                                                    ("h2", "H2"),
                                                    ("h3", "H3"),
                                                    ("h4", "H4"),
                                                ],
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "paragraph_block",
                                wagtail.blocks.RichTextBlock(
                                    icon="fa-paragraph",
                                    template="blocks/paragraph_block.html",
                                ),
                            ),
                            (
                                "image_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                        (
                                            "attribution",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "block_quote",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("text", wagtail.blocks.TextBlock()),
                                        (
                                            "attribute_name",
                                            wagtail.blocks.CharBlock(
                                                blank=True,
                                                label="e.g. Mary Berry",
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "embed_block",
                                wagtail.embeds.blocks.EmbedBlock(
                                    help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
                                    icon="fa-s15",
                                    template="blocks/embed_block.html",
                                ),
                            ),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Page body",
                    ),
                ),
                ("address", models.TextField()),
                (
                    "lat_long",
                    models.CharField(
                        help_text="Separados por vírgula lat/long. (Ex. 64.144367, -21.939182)                    Clique com o botão direito do mouse em Google Maps e selecione 'O que é aqui'",
                        max_length=36,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_lat_long",
                                message="Latitude e Longetitude deve ser um numérico separado por vírgula",
                                regex="^(\\-?\\d+(\\.\\d+)?),\\s*(\\-?\\d+(\\.\\d+)?)$",
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.TextField(blank=True, help_text="E-mail para contato"),
                ),
                (
                    "phone",
                    models.TextField(
                        blank=True,
                        help_text="Número de telefone para contato, formato (xx)xxxxx-xxxx",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Somente modo paisagem; largura horizontal entre 1000px and 3000px.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="LocationOperatingHours",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("SEG", "Segunda-Feira"),
                            ("TER", "Terça-Feira"),
                            ("QUA", "Quarta-Feira"),
                            ("QUI", "Quinta-Feira"),
                            ("SEX", "Sexta-Feira"),
                            ("SAB", "Sábado"),
                            ("DOM", "Domingo"),
                        ],
                        default="SEG",
                        max_length=4,
                    ),
                ),
                ("opening_time", models.TimeField(blank=True, null=True)),
                ("closing_time", models.TimeField(blank=True, null=True)),
                (
                    "closed",
                    models.BooleanField(
                        blank=True,
                        help_text="Marque se o local estiver fechado neste dia",
                        verbose_name="Closed?",
                    ),
                ),
                (
                    "location",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hours_of_operation",
                        to="locations.locationpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
