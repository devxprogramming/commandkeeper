from rest_framework.throttling import UserRateThrottle

class UserBaseRateThrottle(UserRateThrottle):
    def get_cache_key(self, request, view):
        """
        Generates a unique cache key for the request based on user ID and rate scope.
        """
        if request.user.is_authenticated:
            ident = request.user.pk  # Use user ID for authenticated users
        else:
            ident = self.get_ident(request)  # Use IP address for unauthenticated users

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

    def allow_request(self, request, view):
        """
        Adjusts the scope before checking the rate limit.
        """
        if request.user.is_authenticated:
            self.scope = "authenticated"
        else:
            self.scope = "unauthenticated"

        return super().allow_request(request, view)

    def get_rate(self):
        """
        Sets the rate based on the scope.
        """
        if self.scope == "authenticated":
            return "1000/minute"
        elif self.scope == "unauthenticated":
            return "2/minute"
        return None
