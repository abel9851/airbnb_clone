from django.contrib import messages
from django.shortcuts import redirect, reverse, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from rooms import models as room_models
from . import models as review_models
from . import forms


@login_required
def create_review(request, room):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        room = room_models.Room.objects.get_or_none(pk=room)
        if not room:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.room = room
            review.user = request.user
            review.save()
            messages.success(request, "Room reviewed")
            return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))


@login_required
def update_review(request, room, comment):
    review = get_object_or_404(review_models.Review, pk=comment)
    room = room_models.Room.objects.get_or_none(pk=room)

    if request.user != review.user:
        messages.error(request, "You can't")
        return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))

    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST, instance=review)
        if form.is_valid():
            messages.success(request, "Review updated")
            review = form.save()
            review.save()
            return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))
    else:
        form = forms.CreateReviewForm(instance=review)
    return render(request, "reviews/update.html", {"form": form})


@login_required
def delete_review(request, room, comment):
    review = get_object_or_404(review_models.Review, pk=comment)
    room = room_models.Room.objects.get_or_none(pk=room)

    if request.user != review.user:
        messages.error(request, "You can't")
        return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))

    messages.success(request, "Review deleted")
    review.delete()
    return redirect(reverse("places:detail", kwargs={"pk": room.pk}))