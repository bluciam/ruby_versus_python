class AnimalQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, animal_type, name):
        self.queue.append((animal_type, name))
        return (animal_type, name)

    def dequeue_any(self):
        print
        if self.queue == []:
            print "Uhmm, there do no seem to be any more pests!"
        else:
            print "Here is your future headache!"
            animal = self.queue.pop(0)
            print "A " + animal[0] + " named " + animal[1].title()
            return animal

    def dequeue_cat(self):
        print
        for i,k in enumerate(self.queue):
            if self.queue[i][0] == "cat":
                animal = self.queue.pop(i)
                print "Here have this lovely cat named " + \
                    animal[1].title() + "!"
                return animal
        print "Uhmm, there do no seem to be any more masters!"

    def dequeue_dog(self):
        print
        for i,k in enumerate(self.queue):
            if self.queue[i][0] == "dog":
                animal = self.queue.pop(i)
                print "Here have this guardian dog called " + \
                    animal[1].title() + "!"
                return animal
        print "Uhmm, there do no seem to be any more slaves!"


cats_dogs = AnimalQueue()
cats_dogs.enqueue("cat", "arnika")
cats_dogs.enqueue("dog", "bobo")
cats_dogs.enqueue("dog", "chester")
cats_dogs.enqueue("cat", "lucy")
cats_dogs.enqueue("cat", "mindy")
print
print cats_dogs.queue
print cats_dogs.dequeue_dog()
print cats_dogs.dequeue_cat()
print cats_dogs.dequeue_any()
print
print cats_dogs.queue
