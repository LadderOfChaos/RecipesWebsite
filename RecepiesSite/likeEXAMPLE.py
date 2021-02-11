# def like_item(request, pk):
#     item = Item.objects.get(pk=pk)
#
#
#     if Like.objects.filter(item_id=pk).exists():
#         Like.objects.filter(item_id=pk).delete()
#     else:
#         like = Like()
#     like.item = item
#     like.save()
#     return redirect('item details or comment', pk)
