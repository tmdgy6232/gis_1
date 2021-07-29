from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.decorators import profile_ownership_required
from profileapp.models import Profile

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    # 폼 유효성 체크 재정의해서 user 삽입
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    # 동적으로 detail page에 Pk를 물고가기위해 매서드 재정의
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})