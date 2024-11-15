from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Mission, Target
from .serializer import MissionSerializer, TargetSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.Cat:
            return Response({'error': 'Cannot delete a mission assigned to a cat.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['patch'])
    def update_target(self, request, pk=None, target_id=None):
        mission = self.get_object()

        target = mission.targets.filter(id=target_id).first()

        if not target:
            return Response({'error': 'Target not found.'}, status=status.HTTP_404_NOT_FOUND)

        if mission.Complete_state or target.Complete_state:
            return Response({'error': 'Cannot update notes for completed mission or target.'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = TargetSerializer(target, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get('cat_id')
        if not cat_id:
            cat_id = request.data.get('Cat')
        mission.Cat_id = cat_id
        mission.save()
        return Response({'status': 'Cat assigned to mission.'})
