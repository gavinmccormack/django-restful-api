# eventr 


# Okay. 

16/09/21

I've just fired this link over to you by email. I thought I'd write a "Where I got to..."

So events are just sent to the front end by an all() queryset in a bog standard django JSON/GET view.

I didn't hook this up to the REST framework, and I had
a wee bit of trouble working out exactly what defines an instance when populating the database - and therefor how to handle the times aspect.

I haven't used the RESTframework in recent memory, but it seems like it has some standardised components for taking in URL parameters and transfering them into a date range - so I don't think I'd be writing that myself.


Front end? Quite rough. Definitely shows too many items. I suppose all it would need is the filter parameters for dates. Search attributes broadened.

I think I've written this somewhere in comments, but I would be inclined not to pass _all_ of this logic over to the back end. I think given the nature of the data, the client can hold quite a lot of it easily, do front end searching via JS/the client side platform. This would make it very fast and reduce complexity, leverage caching, so on and so forth.



model-api relationship - I had been expecting some kind of unique ID that ties events together - for example 20/20 vision at
toppings book shops. I was hoping they'd have a shared ID between 'instances', but that doesn't seem to be the case. Without
knowledge of the data, or checking them I wouldn't know which field is a good unique key.












Welcome to eventr, the (fictional) Future of Listings for the Web 3.0 era. Development has just started but 
eventr aims to provide a unified listings API for events at partner venues. All partner venues will use the
Spektrix ticketing system to start with.

eventr aims to add hundreds of partners to its listing portal rapidly, and prides itself on its responsive and 
performant user interface and APIs. Some partners may have just one production with hundreds or thousands of 
performances, while others may have hundreds of productions with only one performance each.

## Terminology

A `Source` is a source of data (i.e. a partner venue's ticketing system).

An `Event` is a particular production, for example "Hamlet".

An `EventInstance` is a performance of an `Event`, for example the Wednesday matinee for Hamlet.

## Tasks

1. Clone this repository (please don't use Github to fork it otherwise it'll be too easy for others to find your solution!)

2. Add the `Source` model to Django admin so that you can easily add new sources. For testing purposes, you may wish to use the following Spektrix clients. 

| Partner Name                  | Spektrix Client Name | Spektrix API help page                                      | Spektrix API "Events" endpoint                                |
| ----------------------------- | -------------------- | ----------------------------------------------------------- | ------------------------------------------------------------- |
| Topping & Company Booksellers | toppingbooks         | https://system.spektrix.com/toppingbooks/api/v3/help        | https://system.spektrix.com/toppingbooks/api/v3/events        |
| Mercury Theatre               | mercurytheatre       | https://system.spektrix.com/mercurytheatre/api/v3/help      | https://system.spektrix.com/mercurytheatre/api/v3/events      |
| The Bridge Theatre            | bridgetheatrelondon  | https://system.spektrix.com/bridgetheatrelondon/api/v3/help | https://system.spektrix.com/bridgetheatrelondon/api/v3/events |

3. Create a Django management command to sync events and event instances from all `Source`s and 
create/update them in the eventr database, using the models in the `listings` app. This management command will be
run manually by eventr staff to start with, but you should make sure that nothing unexpected will happen if two
staff members run the management command at the same time.

4. Using Django REST Framework, create views to allow the listings to be searched/browsed. Users will want to search 
by a combination of the following parameters:
	- event name (partial)
	- partner
	- event instances within date range
	- city (NB: there is no field for city in the Spektrix API response but you can assume that all performances from a single `Source` will be in the same city, which can be configured when adding the `Source`)

5. Create an interface for end-users which displays listings using data from DRF views and allows searching as described above. The homepage should display events happening today across all partner venues. We use Vue.js, so if you're already familiar with Vue then please use it. But if you are more comfortable using another frontend framework (or none at all) please feel free to use whichever you prefer. If you choose not to use a frontend framework please bear in mind that we would like to see some Javascript.

6. Publish your code on Github as a private repository and add us to it.

## Guidelines

This doesn't have to be production-ready and you can take shortcuts that make sense in the context of a 
fictional project (although we do want to be able to get a sense for your coding style, so don't take 
too many). We may discuss the approaches you've taken (as well as things you might change
in the future or if you had to scale eventr) at interview. There are bonus points available for good 
git ettiquette.
