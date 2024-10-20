# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class BlogAicontenttemplate(models.Model):
    name = models.CharField(max_length=255)
    prompt_template = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_aicontenttemplate'


class BlogBlogindexpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_blogindexpage'


class BlogBlogindexpagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(BlogBlogindexpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogindexpagerelatedlink'


class BlogBlogpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    intro = models.TextField()
    body = models.TextField()
    date = models.DateField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    ai_content_template = models.ForeignKey(BlogAicontenttemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_blogpage'


class BlogBlogpagecarouselitem(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    embed_url = models.CharField(max_length=200)
    caption = models.TextField()
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(BlogBlogpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogpagecarouselitem'


class BlogBlogpagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(BlogBlogpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogpagerelatedlink'


class BlogBlogpagetag(models.Model):
    content_object = models.ForeignKey(BlogBlogpage, models.DO_NOTHING)
    tag = models.ForeignKey('TaggitTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogpagetag'


class ContactContactformfield(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=16)
    required = models.BooleanField()
    choices = models.TextField()
    default_value = models.CharField(max_length=255)
    help_text = models.CharField(max_length=255)
    page = models.ForeignKey('ContactContactpage', models.DO_NOTHING)
    clean_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contact_contactformfield'


class ContactContactpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    name_organization = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=254)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    post_code = models.CharField(max_length=10)
    intro = models.CharField(max_length=255)
    thank_you_text = models.TextField()
    telephone_2 = models.CharField(max_length=20)
    email_2 = models.CharField(max_length=254)
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_contactpage'


class ContactFormfield(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=16)
    required = models.BooleanField()
    choices = models.TextField()
    default_value = models.CharField(max_length=255)
    help_text = models.CharField(max_length=255)
    page = models.ForeignKey('ContactFormpage', models.DO_NOTHING)
    clean_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contact_formfield'


class ContactFormpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    intro = models.TextField()
    thank_you_text = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_formpage'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class DocumentsGalleryDocumentsindexpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_gallery_documentsindexpage'


class DocumentsGalleryDocumentspage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_gallery_documentspage'


class DocumentsGalleryDocumentspagetag(models.Model):
    content_object = models.ForeignKey(DocumentsGalleryDocumentspage, models.DO_NOTHING)
    tag = models.ForeignKey('TaggitTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'documents_gallery_documentspagetag'


class GalleryGalleryindex(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    intro = models.TextField()
    order_images_by = models.IntegerField()
    collection = models.ForeignKey('WagtailcoreCollection', models.DO_NOTHING, blank=True, null=True)
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    images_per_page = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gallery_galleryindex'


class GalleryPhotogalleryindexpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gallery_photogalleryindexpage'


class PagesAdvert(models.Model):
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField()
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    button_text = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_advert'


class PagesContentblock(models.Model):
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    body = models.TextField()
    summary = models.TextField()
    slug = models.CharField(max_length=50)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_contentblock'


class PagesFaqspage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'pages_faqspage'


class PagesHomepage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    main_description = models.TextField()
    background_video = models.ForeignKey('WagtailmediaMedia', models.DO_NOTHING, blank=True, null=True)
    main_title = models.CharField(max_length=255)
    portfolio_items = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_homepage'


class PagesHomepagecarouselitem(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    embed_url = models.CharField(max_length=200)
    caption = models.TextField()
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PagesHomepage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_homepagecarouselitem'


class PagesHomepagecontentitem(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    summary = models.TextField()
    slug = models.CharField(max_length=50)
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PagesHomepage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_homepagecontentitem'


class PagesHomepagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PagesHomepage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_homepagerelatedlink'


class PagesSitebranding(models.Model):
    site_name = models.CharField(max_length=250, blank=True, null=True)
    logo = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    site = models.OneToOneField('WagtailcoreSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_sitebranding'


class PagesSocialmediasettings(models.Model):
    facebook = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    github = models.CharField(max_length=255, blank=True, null=True)
    facebook_appid = models.CharField(max_length=255, blank=True, null=True)
    site = models.OneToOneField('WagtailcoreSite', models.DO_NOTHING)
    twitter = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_socialmediasettings'


class PagesStandardindexpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    subtitle = models.CharField(max_length=255)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    template_string = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pages_standardindexpage'


class PagesStandardindexpagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PagesStandardindexpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_standardindexpagerelatedlink'


class PagesStandardpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    subtitle = models.CharField(max_length=255)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    template_string = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'pages_standardpage'


class PagesStandardpagecarouselitem(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    embed_url = models.CharField(max_length=200)
    caption = models.TextField()
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PagesStandardpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_standardpagecarouselitem'


class PagesStandardpagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PagesStandardpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_standardpagerelatedlink'


class PagesTestimonial(models.Model):
    link_external = models.CharField(max_length=200)
    name = models.CharField(max_length=150)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    photo = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'pages_testimonial'


class PagesTestimonialpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_testimonialpage'


class PagesVideogallerypage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_videogallerypage'


class PagesVideogallerypagecarouselitem(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    embed_url = models.CharField(max_length=200)
    caption = models.TextField()
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PagesVideogallerypage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_videogallerypagecarouselitem'


class PeoplePersonindexpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    subtitle = models.CharField(max_length=255)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people_personindexpage'


class PeoplePersonindexpagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PeoplePersonindexpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_personindexpagerelatedlink'


class PeoplePersonpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    name_organization = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=254)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    post_code = models.CharField(max_length=10)
    intro = models.TextField()
    biography = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('PeoplePersonrole', models.DO_NOTHING, blank=True, null=True)
    telephone_2 = models.CharField(max_length=20)
    email_2 = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'people_personpage'


class PeoplePersonpagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(PeoplePersonpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_personpagerelatedlink'


class PeoplePersonpagetag(models.Model):
    content_object = models.ForeignKey(PeoplePersonpage, models.DO_NOTHING)
    tag = models.ForeignKey('TaggitTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_personpagetag'


class PeoplePersonrole(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'people_personrole'


class ProductsProductindexpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    subtitle = models.CharField(max_length=255)
    intro = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_productindexpage'


class ProductsProductindexpagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(ProductsProductindexpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_productindexpagerelatedlink'


class ProductsProductpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    price = models.CharField(max_length=255)
    description = models.TextField()
    feed_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    intro = models.CharField(max_length=255)
    link_demo = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'products_productpage'


class ProductsProductpagerelatedlink(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    link_external = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    link_document = models.ForeignKey('WagtaildocsDocument', models.DO_NOTHING, blank=True, null=True)
    link_page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(ProductsProductpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_productpagerelatedlink'


class ProductsProductpagetag(models.Model):
    content_object = models.ForeignKey(ProductsProductpage, models.DO_NOTHING)
    tag = models.ForeignKey('TaggitTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_productpagetag'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    tos = models.BooleanField()
    country = models.CharField(max_length=255)
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)


class WagtailFeedsRssfeedssettings(models.Model):
    feed_app_label = models.CharField(max_length=255, blank=True, null=True)
    feed_model_name = models.CharField(max_length=255, blank=True, null=True)
    feed_title = models.CharField(max_length=255, blank=True, null=True)
    feed_link = models.CharField(max_length=255, blank=True, null=True)
    feed_description = models.CharField(max_length=255, blank=True, null=True)
    feed_author_email = models.CharField(max_length=255, blank=True, null=True)
    feed_author_link = models.CharField(max_length=255, blank=True, null=True)
    feed_item_description_field = models.CharField(max_length=255, blank=True, null=True)
    feed_item_content_field = models.CharField(max_length=255, blank=True, null=True)
    site = models.OneToOneField('WagtailcoreSite', models.DO_NOTHING)
    feed_image_in_content = models.BooleanField()
    feed_item_date_field = models.CharField(max_length=255)
    is_feed_item_date_field_datetime = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'wagtail_feeds_rssfeedssettings'


class WagtailLocalizeLocalesynchronization(models.Model):
    locale = models.OneToOneField('WagtailcoreLocale', models.DO_NOTHING)
    sync_from = models.ForeignKey('WagtailcoreLocale', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_localesynchronization'


class WagtailLocalizeOverridablesegment(models.Model):
    order = models.PositiveIntegerField()
    data_json = models.TextField()
    context = models.ForeignKey('WagtailLocalizeTranslationcontext', models.DO_NOTHING)
    source = models.ForeignKey('WagtailLocalizeTranslationsource', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_overridablesegment'


class WagtailLocalizeRelatedobjectsegment(models.Model):
    order = models.PositiveIntegerField()
    context = models.ForeignKey('WagtailLocalizeTranslationcontext', models.DO_NOTHING)
    object = models.ForeignKey('WagtailLocalizeTranslatableobject', models.DO_NOTHING)
    source = models.ForeignKey('WagtailLocalizeTranslationsource', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_relatedobjectsegment'


class WagtailLocalizeSegmentoverride(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    data_json = models.TextField()
    has_error = models.BooleanField()
    field_error = models.TextField()
    context = models.ForeignKey('WagtailLocalizeTranslationcontext', models.DO_NOTHING, blank=True, null=True)
    last_translated_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    locale = models.ForeignKey('WagtailcoreLocale', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_segmentoverride'


class WagtailLocalizeString(models.Model):
    data_hash = models.CharField(max_length=32)
    data = models.TextField()
    locale = models.ForeignKey('WagtailcoreLocale', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_string'
        unique_together = (('locale', 'data_hash'),)


class WagtailLocalizeStringsegment(models.Model):
    order = models.PositiveIntegerField()
    attrs = models.TextField()
    context = models.ForeignKey('WagtailLocalizeTranslationcontext', models.DO_NOTHING)
    source = models.ForeignKey('WagtailLocalizeTranslationsource', models.DO_NOTHING)
    string = models.ForeignKey(WagtailLocalizeString, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_stringsegment'


class WagtailLocalizeStringtranslation(models.Model):
    data = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    context = models.ForeignKey('WagtailLocalizeTranslationcontext', models.DO_NOTHING, blank=True, null=True)
    locale = models.ForeignKey('WagtailcoreLocale', models.DO_NOTHING)
    translation_of = models.ForeignKey(WagtailLocalizeString, models.DO_NOTHING)
    tool_name = models.CharField(max_length=255)
    translation_type = models.CharField(max_length=20)
    last_translated_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    field_error = models.TextField()
    has_error = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'wagtail_localize_stringtranslation'
        unique_together = (('locale', 'translation_of', 'context'),)


class WagtailLocalizeTemplate(models.Model):
    uuid = models.CharField(unique=True, max_length=32)
    template = models.TextField()
    template_format = models.CharField(max_length=100)
    string_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wagtail_localize_template'


class WagtailLocalizeTemplatesegment(models.Model):
    order = models.PositiveIntegerField()
    context = models.ForeignKey('WagtailLocalizeTranslationcontext', models.DO_NOTHING)
    source = models.ForeignKey('WagtailLocalizeTranslationsource', models.DO_NOTHING)
    template = models.ForeignKey(WagtailLocalizeTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_templatesegment'


class WagtailLocalizeTranslatableobject(models.Model):
    translation_key = models.CharField(primary_key=True, max_length=32)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_translatableobject'
        unique_together = (('content_type', 'translation_key'),)


class WagtailLocalizeTranslation(models.Model):
    uuid = models.CharField(unique=True, max_length=32)
    created_at = models.DateTimeField()
    translations_last_updated_at = models.DateTimeField(blank=True, null=True)
    destination_last_updated_at = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    source = models.ForeignKey('WagtailLocalizeTranslationsource', models.DO_NOTHING)
    target_locale = models.ForeignKey('WagtailcoreLocale', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_translation'
        unique_together = (('source', 'target_locale'),)


class WagtailLocalizeTranslationcontext(models.Model):
    path_id = models.CharField(max_length=32)
    path = models.TextField()
    object = models.ForeignKey(WagtailLocalizeTranslatableobject, models.DO_NOTHING)
    field_path = models.TextField()

    class Meta:
        managed = False
        db_table = 'wagtail_localize_translationcontext'
        unique_together = (('object', 'path_id'),)


class WagtailLocalizeTranslationlog(models.Model):
    created_at = models.DateTimeField()
    locale = models.ForeignKey('WagtailcoreLocale', models.DO_NOTHING)
    page_revision = models.ForeignKey('WagtailcorePagerevision', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('WagtailLocalizeTranslationsource', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_translationlog'


class WagtailLocalizeTranslationsource(models.Model):
    object_repr = models.TextField()
    content_json = models.TextField()
    created_at = models.DateTimeField()
    locale = models.ForeignKey('WagtailcoreLocale', models.DO_NOTHING)
    object = models.ForeignKey(WagtailLocalizeTranslatableobject, models.DO_NOTHING)
    specific_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    last_updated_at = models.DateTimeField()
    schema_version = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtail_localize_translationsource'
        unique_together = (('object', 'locale'),)


class WagtailadminAdmin(models.Model):

    class Meta:
        managed = False
        db_table = 'wagtailadmin_admin'


class WagtailcoreCollection(models.Model):
    path = models.CharField(unique=True, max_length=255)
    depth = models.PositiveIntegerField()
    numchild = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collection'


class WagtailcoreCollectionviewrestriction(models.Model):
    restriction_type = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collectionviewrestriction'


class WagtailcoreCollectionviewrestrictionGroups(models.Model):
    collectionviewrestriction = models.ForeignKey(WagtailcoreCollectionviewrestriction, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collectionviewrestriction_groups'
        unique_together = (('collectionviewrestriction', 'group'),)


class WagtailcoreComment(models.Model):
    text = models.TextField()
    contentpath = models.TextField()
    position = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    resolved_at = models.DateTimeField(blank=True, null=True)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING)
    resolved_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    revision_created = models.ForeignKey('WagtailcorePagerevision', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_comment'


class WagtailcoreCommentreply(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comment = models.ForeignKey(WagtailcoreComment, models.DO_NOTHING)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_commentreply'


class WagtailcoreGroupapprovaltask(models.Model):
    task_ptr = models.OneToOneField('WagtailcoreTask', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupapprovaltask'


class WagtailcoreGroupapprovaltaskGroups(models.Model):
    groupapprovaltask = models.ForeignKey(WagtailcoreGroupapprovaltask, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupapprovaltask_groups'
        unique_together = (('groupapprovaltask', 'group'),)


class WagtailcoreGroupcollectionpermission(models.Model):
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupcollectionpermission'
        unique_together = (('group', 'collection', 'permission'),)


class WagtailcoreGrouppagepermission(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING)
    permission_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wagtailcore_grouppagepermission'
        unique_together = (('group', 'page', 'permission_type'),)


class WagtailcoreLocale(models.Model):
    language_code = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'wagtailcore_locale'


class WagtailcoreModellogentry(models.Model):
    label = models.TextField()
    action = models.CharField(max_length=255)
    data_json = models.TextField()
    timestamp = models.DateTimeField()
    content_changed = models.BooleanField()
    deleted = models.BooleanField()
    object_id = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_modellogentry'


class WagtailcorePage(models.Model):
    path = models.CharField(unique=True, max_length=255)
    depth = models.PositiveIntegerField()
    numchild = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    live = models.BooleanField()
    has_unpublished_changes = models.BooleanField()
    url_path = models.TextField()
    seo_title = models.CharField(max_length=255)
    show_in_menus = models.BooleanField()
    search_description = models.TextField()
    go_live_at = models.DateTimeField(blank=True, null=True)
    expire_at = models.DateTimeField(blank=True, null=True)
    expired = models.BooleanField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    owner = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    locked = models.BooleanField()
    latest_revision_created_at = models.DateTimeField(blank=True, null=True)
    first_published_at = models.DateTimeField(blank=True, null=True)
    live_revision = models.ForeignKey('WagtailcorePagerevision', models.DO_NOTHING, blank=True, null=True)
    last_published_at = models.DateTimeField(blank=True, null=True)
    draft_title = models.CharField(max_length=255)
    locked_at = models.DateTimeField(blank=True, null=True)
    locked_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    translation_key = models.CharField(max_length=32)
    locale = models.ForeignKey(WagtailcoreLocale, models.DO_NOTHING)
    alias_of = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_page'
        unique_together = (('translation_key', 'locale'),)


class WagtailcorePagelogentry(models.Model):
    label = models.TextField()
    action = models.CharField(max_length=255)
    data_json = models.TextField()
    timestamp = models.DateTimeField()
    content_changed = models.BooleanField()
    deleted = models.BooleanField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    page_id = models.IntegerField()
    revision_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pagelogentry'


class WagtailcorePagerevision(models.Model):
    submitted_for_moderation = models.BooleanField()
    created_at = models.DateTimeField()
    content_json = models.TextField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    approved_go_live_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pagerevision'


class WagtailcorePagesubscription(models.Model):
    comment_notifications = models.BooleanField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pagesubscription'
        unique_together = (('page', 'user'),)


class WagtailcorePageviewrestriction(models.Model):
    password = models.CharField(max_length=255)
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    restriction_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pageviewrestriction'


class WagtailcorePageviewrestrictionGroups(models.Model):
    pageviewrestriction = models.ForeignKey(WagtailcorePageviewrestriction, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pageviewrestriction_groups'
        unique_together = (('pageviewrestriction', 'group'),)


class WagtailcoreSite(models.Model):
    hostname = models.CharField(max_length=255)
    port = models.IntegerField()
    is_default_site = models.BooleanField()
    root_page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    site_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailcore_site'
        unique_together = (('hostname', 'port'),)


class WagtailcoreTask(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_task'


class WagtailcoreTaskstate(models.Model):
    status = models.CharField(max_length=50)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    page_revision = models.ForeignKey(WagtailcorePagerevision, models.DO_NOTHING)
    task = models.ForeignKey(WagtailcoreTask, models.DO_NOTHING)
    workflow_state = models.ForeignKey('WagtailcoreWorkflowstate', models.DO_NOTHING)
    finished_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'wagtailcore_taskstate'


class WagtailcoreWorkflow(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflow'


class WagtailcoreWorkflowpage(models.Model):
    page = models.OneToOneField(WagtailcorePage, models.DO_NOTHING, primary_key=True)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowpage'


class WagtailcoreWorkflowstate(models.Model):
    created_at = models.DateTimeField()
    current_task_state = models.OneToOneField(WagtailcoreTaskstate, models.DO_NOTHING, blank=True, null=True)
    page = models.OneToOneField(WagtailcorePage, models.DO_NOTHING)
    requested_by = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowstate'


class WagtailcoreWorkflowtask(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    task = models.ForeignKey(WagtailcoreTask, models.DO_NOTHING)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowtask'
        unique_together = (('workflow', 'task'),)


class WagtaildocsDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    uploaded_by_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    file_hash = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wagtaildocs_document'


class WagtaildocsUploadeddocument(models.Model):
    file = models.CharField(max_length=200)
    uploaded_by_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtaildocs_uploadeddocument'


class WagtailembedsEmbed(models.Model):
    url = models.TextField()
    max_width = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=10)
    html = models.TextField()
    title = models.TextField()
    author_name = models.TextField()
    provider_name = models.TextField()
    thumbnail_url = models.TextField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField()
    hash = models.CharField(unique=True, max_length=32)
    cache_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailembeds_embed'


class WagtailformsFormsubmission(models.Model):
    form_data = models.TextField()
    submit_time = models.DateTimeField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailforms_formsubmission'


class WagtailimagesImage(models.Model):
    title = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField()
    focal_point_x = models.PositiveIntegerField(blank=True, null=True)
    focal_point_y = models.PositiveIntegerField(blank=True, null=True)
    focal_point_width = models.PositiveIntegerField(blank=True, null=True)
    focal_point_height = models.PositiveIntegerField(blank=True, null=True)
    uploaded_by_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    file_hash = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wagtailimages_image'


class WagtailimagesRendition(models.Model):
    file = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    focal_point_key = models.CharField(max_length=16)
    filter_spec = models.CharField(max_length=255)
    image = models.ForeignKey(WagtailimagesImage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailimages_rendition'
        unique_together = (('image', 'filter_spec', 'focal_point_key'),)


class WagtailimagesUploadedimage(models.Model):
    file = models.CharField(max_length=200)
    uploaded_by_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailimages_uploadedimage'


class WagtailmediaMedia(models.Model):
    title = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    type = models.CharField(max_length=255)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    uploaded_by_user = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    duration = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wagtailmedia_media'


class WagtailredirectsRedirect(models.Model):
    old_path = models.CharField(max_length=255)
    is_permanent = models.BooleanField()
    redirect_link = models.CharField(max_length=255)
    redirect_page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey(WagtailcoreSite, models.DO_NOTHING, blank=True, null=True)
    automatically_created = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    redirect_page_route_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailredirects_redirect'
        unique_together = (('old_path', 'site'),)


class WagtailsearchIndexentry(models.Model):
    object_id = models.CharField(max_length=50)
    title_norm = models.FloatField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    autocomplete = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry'
        unique_together = (('content_type', 'object_id'),)


class WagtailsearchIndexentryFts(models.Model):
    autocomplete = models.TextField(blank=True, null=True)  # This field type is a guess.
    body = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry_fts'


class WagtailsearchIndexentryFtsConfig(models.Model):
    k = models.TextField(primary_key=True)  # This field type is a guess.
    v = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry_fts_config'


class WagtailsearchIndexentryFtsContent(models.Model):
    c0 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c2 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry_fts_content'


class WagtailsearchIndexentryFtsData(models.Model):
    block = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry_fts_data'


class WagtailsearchIndexentryFtsDocsize(models.Model):
    sz = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry_fts_docsize'


class WagtailsearchIndexentryFtsIdx(models.Model):
    segid = models.TextField()  # This field type is a guess.
    term = models.TextField()  # This field type is a guess.
    pgno = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry_fts_idx'


class WagtailsearchQuery(models.Model):
    query_string = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_query'


class WagtailsearchQuerydailyhits(models.Model):
    date = models.DateField()
    hits = models.IntegerField()
    query = models.ForeignKey(WagtailsearchQuery, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_querydailyhits'
        unique_together = (('query', 'date'),)


class WagtailsearchpromotionsSearchpromotion(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    query = models.ForeignKey(WagtailsearchQuery, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailsearchpromotions_searchpromotion'


class WagtailusersUserprofile(models.Model):
    submitted_notifications = models.BooleanField()
    approved_notifications = models.BooleanField()
    rejected_notifications = models.BooleanField()
    user = models.OneToOneField(UsersUser, models.DO_NOTHING)
    preferred_language = models.CharField(max_length=10)
    current_time_zone = models.CharField(max_length=40)
    avatar = models.CharField(max_length=100)
    updated_comments_notifications = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'wagtailusers_userprofile'
