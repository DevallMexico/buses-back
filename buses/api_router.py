from rest_framework.routers import DefaultRouter
from users.api.views import UserViewSet
from travels.api.views import TravelsViewSet, TravelSchedulesViewSet
from bus.api.views import BusesViewSet
from drivers.api.views import DriversViewSet
from seatings.api.views import SeatingsViewSet

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("drivers", DriversViewSet)
router.register("seatings", SeatingsViewSet)
router.register("travels", TravelsViewSet)
router.register("buses", BusesViewSet)
router.register("schedules", TravelSchedulesViewSet)

app_name = "api"
urlpatterns = router.urls