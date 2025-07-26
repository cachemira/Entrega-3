from django.urls import path

from .views import (saludo, saludo_con_template, crear_familiar, inicio, crear_curso, crear_estudiante, buscar_cursos, cursos, about, buscar_libros,
                    LibroCreateView, LibroListView, LibroDeleteView, LibroDetailView, LibroUpdateView, CursoDetailView, CursoUpdateView, CursoDeleteView)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
    path('crear-curso/', crear_curso, name= 'crear-curso'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('cursos/', cursos, name='cursos'),
    path('cursos/buscar/', buscar_cursos, name='buscar-cursos'),
    path('libros/buscar/', buscar_libros, name='buscar-libros'),
    path('about/', about, name='about'),

    #url con vistas basadas en clase
    path('listar-libros/', LibroListView.as_view(), name= 'listar-libros'),
    path('crear-libro/', LibroCreateView.as_view(), name= 'crear-libro'),
    path('detalle-libro/<int:pk>', LibroDetailView.as_view(), name= 'detalle-libro'),
    path('editar-libro/<int:pk>/', LibroUpdateView.as_view(), name= 'editar-libro'),
    path('eliminar-libro/<int:pk>/', LibroDeleteView.as_view(), name= 'eliminar-libro'),
    path('detalle-curso/<int:pk>', CursoDetailView.as_view(), name= 'detalle-curso'),
    path('editar-curso/<int:pk>/', CursoUpdateView.as_view(), name= 'editar-curso'),
    path('eliminar-curso/<int:pk>/', CursoDeleteView.as_view(), name= 'eliminar-curso'),
]

