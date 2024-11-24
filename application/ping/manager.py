from asyncio import gather
from .entities import HealthStatus


class PingManager:
    async def _perform_application_health_check(self) -> HealthStatus:
        """Perform application health check

        Ensure that the application is running

        Returns:
            HealthStatus: The health status of the application
        """
        return HealthStatus(name="application", is_healthy=True)

    async def get_health_status(self) -> list[HealthStatus]:
        """Get health status

        Get the health status of the application
        """
        health = await gather(
            self._perform_application_health_check(),
        )

        return list(health)