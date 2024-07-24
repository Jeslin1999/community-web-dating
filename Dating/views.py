from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import GenderselectForm,MessageForm, MediaForm
from account.forms import LoginForm
from django.views.generic import FormView, ListView, DetailView, CreateView, DeleteView, TemplateView
from .models import Genderselect, Friendconnection, Message, Media
from account.models import User,Employee, Jobseeker
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin




class GenderselectView(LoginRequiredMixin, FormView):
    template_name = 'Dating/selectgender.html'
    form_class = GenderselectForm
    success_url = reverse_lazy('Dating:gridview')
    def form_valid(self, form):
        genderselect, created = Genderselect.objects.update_or_create(
            user=self.request.user,
            defaults={'genderselect': form.cleaned_data['genderselect']}
        )
        return super().form_valid(form)
    

class LoginView(FormView):
    template_name = 'account/Login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
                login(self.request, user)
                gender_selection = Genderselect.objects.filter(user=self.request.user.id)
                if gender_selection.exists():
                    return redirect('Dating:gridview')
                else:
                    return redirect('Dating:selectgender') 
        else:
            return self.form_invalid(form) 


class Gridview(LoginRequiredMixin,ListView):
    model = User, Genderselect
    template_name = 'Dating/gridview.html'
    context_object_name = 'users'

    def get_queryset(self):
        gender_selection = Genderselect.objects.filter(user=self.request.user.id).first()
        if gender_selection:
                if gender_selection.genderselect == 'B':
                    return User.objects.all().exclude(id=self.request.user.id)

                elif gender_selection.genderselect == 'M':
                    return User.objects.filter(gender='Male').exclude(id=self.request.user.id)

                elif gender_selection.genderselect == 'F':
                    return User.objects.filter(gender='Female').exclude(id=self.request.user.id)
                
                queryset = queryset.prefetch_related('employee', 'jobseeker')
            
                return queryset
        
        return User.objects.none()
    

class LocationGridview(LoginRequiredMixin, ListView):
    model = User, Genderselect
    template_name = 'Dating/location.html'
    context_object_name = 'users'

    def get_queryset(self):
        gender_selection = Genderselect.objects.filter(user=self.request.user.id).first()
        queryset = User.objects.all().exclude(id=self.request.user.id)
        
        if gender_selection:
            if gender_selection.genderselect == 'B':
                location = self.request.GET.get('location')
                if location:
                    queryset = queryset.filter(location=location)
                
            elif gender_selection.genderselect == 'M':
                location = self.request.GET.get('location')
                queryset = queryset.filter(gender='Male')
                if location:
                    queryset = queryset.filter(location=location)

            elif gender_selection.genderselect == 'F':
                location = self.request.GET.get('location')
                queryset = queryset.filter(gender='Female')
                if location:
                    queryset = queryset.filter(location=location)
     
        return queryset


class EducationGridview(LoginRequiredMixin, ListView):
    model = User, Genderselect
    template_name = 'Dating/education.html'
    context_object_name = 'users'

    def get_queryset(self):
        gender_selection = Genderselect.objects.filter(user=self.request.user.id).first()
        queryset = User.objects.all().exclude(id=self.request.user.id)
        
        if gender_selection:
            if gender_selection.genderselect == 'B':
                qualification = self.request.GET.get('qualification')
                if qualification:
                    queryset = queryset.filter(qualification=qualification)
                
            elif gender_selection.genderselect == 'M':
                qualification = self.request.GET.get('qualification')
                queryset = queryset.filter(gender='Male')
                if qualification:
                    queryset = queryset.filter(qualification=qualification)

            elif gender_selection.genderselect == 'F':
                qualification = self.request.GET.get('qualification')
                queryset = queryset.filter(gender='Female')
                if qualification:
                    queryset = queryset.filter(qualification=qualification)
     
        return queryset
               


class AllGridview(LoginRequiredMixin,ListView):
    model = User, Genderselect
    template_name = 'Dating/all_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        gender_selection = Genderselect.objects.filter(user=self.request.user.id).first()
        if gender_selection:
                if gender_selection.genderselect == 'B':
                    return User.objects.all().exclude(id=self.request.user.id)

                elif gender_selection.genderselect == 'M':
                    return User.objects.filter(gender='Male').exclude(id=self.request.user.id)

                elif gender_selection.genderselect == 'F':
                    return User.objects.filter(gender='Female').exclude(id=self.request.user.id)
                
                queryset = queryset.prefetch_related('employee', 'jobseeker')
            
                return queryset
        
        return User.objects.none()
    

class UserDetailView(DetailView):
    model = User
    template_name = 'Dating/user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['user']
        
        user.employee_details = Employee.objects.filter(user=user).first()
        user.jobseeker_details = Jobseeker.objects.filter(user=user).first()
        user.media_details = Media.objects.filter(user=user).all()
        
        return context
    

class GalleryView(LoginRequiredMixin, View):
    template_name = 'Dating/gallery.html'

    def get(self, request, *args, **kwargs):
        form = MediaForm()
        media = Media.objects.filter(user=request.user).order_by('-timestamp')
        return render(request, self.template_name, {'form': form, 'media': media})

    def post(self, request, *args, **kwargs):
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            media_instance = form.save(commit=False)
            media_instance.user = request.user
            media_instance.save()
            return redirect(reverse_lazy('Dating:gallery'))
        media = Media.objects.filter(user=request.user).order_by('-timestamp')
        return render(request, self.template_name, {'form': form, 'media': media})


class MediaDeleteView(LoginRequiredMixin, DeleteView):
    model = Media
    success_url = reverse_lazy('Dating:gallery')
    template_name = 'Dating/gallery.html'

    def get_queryset(self):
        # Only allow deletion of media belonging to the current user
        return Media.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('Dating:gallery')
    

class SendrequestView(LoginRequiredMixin, CreateView):
    model = Friendconnection
    fields = []

    def form_valid(self, form):
        send_to_user = get_object_or_404(User, id=self.kwargs['user_id'])
        friend_request, created = Friendconnection.objects.get_or_create(send_by=self.request.user, send_to=send_to_user)
        if created:
            return redirect('Dating:user_detail', pk=self.kwargs['user_id'])
        else:
            return redirect('Dating:user_detail', pk=self.kwargs['user_id'])

    def form_invalid(self, form):
        return redirect('Dating:user_detail', pk=self.kwargs['user_id'])
    

class Accepthtmlview(LoginRequiredMixin, TemplateView):
    template_name = 'Dating/request_re.html'
    def get(self, request):
        user = request.user
        pending_requests = Friendconnection.objects.filter(send_to=user, status=False)
        request_senders = [request.send_by for request in pending_requests]

        context = {
            'pending_requests': pending_requests,
            'request_senders': request_senders,
            'count': pending_requests.count()
        }
        return render(request, 'Dating/request_re.html', context)
    

# class AcceptRequestView(LoginRequiredMixin, UpdateView):
#     model = Friendconnection
#     fields = ['status']

#     def get_object(self, queryset=None):
#         friend_request = get_object_or_404(Friendconnection, id=self.kwargs['request_id'], send_to=self.request.user)
#         return friend_request

#     def form_valid(self, form):
#         form.instance.status = True
#         form.instance.save()
#         return redirect('Dating:user_detail', pk=self.request.user.id)

#     def form_invalid(self, form):
#         return redirect('Dating:user_detail', pk=self.request.user.id)
    

class AcceptRequestView(LoginRequiredMixin, View):
    model = Friendconnection
    fields = [] 
    success_url = reverse_lazy('Dating:gridview')

    def get_object(self, queryset=None):
        return get_object_or_404(Friendconnection, id=self.kwargs['request_id'], send_to=self.request.user)

    def form_valid(self, form):
        action = self.kwargs.get('action', 'accept') 
        friend_request = super().self.get_object()
        
        if action == 'accept':
            friend_request.status = True
            friend_request.save()
            
        elif action == 'reject':
            friend_request.delete() 
        
        return redirect('Dating:accept_requests', pk=self.request.user.id)

    def form_invalid(self, form):
        return redirect('Dating:user_detail', pk=self.request.user.id)
    

class RejectRequestView(LoginRequiredMixin, View):
    model = Friendconnection
    fields = [] 

    def post(self,request, request_id):
        friend_request = get_object_or_404(Friendconnection, id=request_id)
        if friend_request.send_by == request.user:
            friend_request.delete()
        return redirect(reverse_lazy('Dating:accept_requests'))
    

class FriendsListView(View):
    def get(self, request):
        user = request.user
        friends = Friendconnection.objects.filter(send_by=user, status=True) | Friendconnection.objects.filter(send_to=user, status=True)
        friends_list = []
        for friend in friends:
            if friend.send_by == user:
                friends_list.append(friend.send_to)
            else:
                friends_list.append(friend.send_by)
        context = {'friends': friends_list}
        return render(request, '', context)
    

class Messageview(LoginRequiredMixin, TemplateView):
    template_name = 'Dating/chat_room.html'

    def chat_room(request, user_id):
        receiver = User.objects.get(pk=user_id)
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.sender = request.user
                message.receiver = receiver
                message.save()
                return redirect('chat_room', user_id=user_id)
        else:
            form = MessageForm()

        messages = Message.objects.filter(
            sender=request.user, receiver=receiver
        ).union(
            Message.objects.filter(sender=receiver, receiver=request.user)
        ).order_by('timestamp')

        return render(request, 'chat_room.html', {
            'form': form,
            'messages': messages,
            'receiver': receiver
        })