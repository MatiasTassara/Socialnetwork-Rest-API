from django.db import models

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)


class User(models.Model):
    # el id igualmente se genera automatico si no se explicita
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField(unique=True, default='none')
    password = models.CharField(max_length=30)
    relationships = models.ManyToManyField('self',
                                           through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')
    #profile_image = models.ImageField(upload_to='')#ver argumentos
    average = models.FloatField(default=0)

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def add_relationship(self, user, status):
        relationship, created = Relationship.objects.get_or_create(
            from_user=self,
            to_user=user,
            status=status)
        return relationship

    def remove_relationship(self, user, status):
        Relationship.objects.filter(
            from_user=self,
            to_user=user,
            status=status).delete()
        return

    def get_relationships(self, status):
        return self.relationships.filter(
            to_people__status=status,
            to_people__from_user=self)

    def get_related_to(self, status):
        return self.related_to.filter( #sin related name aca usariamos 'user_set' en vez de 'related_to'
            from_people__status=status,
            from_people__to_user=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

# hacemos followers = instance_user.get_followers()
    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)


class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='from_people',on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_people',on_delete=models.CASCADE)
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='', null=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)




class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=300)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)


class Points(models.Model):
    user = models.ForeignKey(User, related_name='user_points', on_delete=models.CASCADE)




