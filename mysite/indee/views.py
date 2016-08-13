from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm, NameForm

from .models import Document
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from wand.image import Image

import os,string
from utils import get_image_path_for_doc, get_image_folder_for_doc

# To be removed : just for printing
from django.http import HttpResponse


@login_required
def index(request):
    current_user = request.user
    documents = Document.objects.filter(user=current_user)
    return render(request, 'indee/index.html', {
        'foo': 'bar',
        'documents': documents,
        'SITE_URL' : request.get_host()
    })


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid() and request.FILES['upload_file'].content_type=="application/pdf":
            current_user = request.user
            newdoc = Document(docfile=request.FILES['upload_file'])
            newdoc.name = request.FILES['upload_file'].name
            newdoc.user = current_user
            newdoc.save()

            file_url = newdoc.docfile.url[1:]  # Removes first / ==> media/documents/2016/10/08/test.pdf
            with Image(filename=file_url) as img:

                dest_folder = get_image_folder_for_doc(file_url)  # Returns media/doc_images/2016/10/08
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                image_path = get_image_path_for_doc(file_url)   # Returns media/doc_images/2016/10/08/test.pdf

                pages = len(img.sequence)
                if(pages > 1):
                    image = Image(
                        width=img.width,
                        height=img.height * pages,
                    )

                    for i in xrange(pages):
                        image.composite(
                            img.sequence[i],
                            top=img.height * i,
                            left=0
                        )

                    image.compression_quality = 95
                    image.format = 'jpg'
                    image.save(filename=image_path)
                else:
                    img.compression_quality = 95
                    img.format = 'jpg'
                    img.width = img.width
                    img.height = img.height
                    img.save(filename=image_path)

                newdoc.imagefile = "/"+image_path
                newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('indee:document-listing'))
        else:
            form = UploadFileForm("Form is not valid")
    else:
        form = UploadFileForm()
    return render(request, 'indee/upload.html', {
        'form': form,
    })


@login_required
def delete_documents(request):
    Document.objects.all().delete()
    return HttpResponse("Deleted !!")


def public_viewer(request, pdf_id):
    pdf_id = int(pdf_id)
    document = Document.objects.get(pk=pdf_id)
    return render(request, 'indee/viewer.html', {
        'document': document,
    })