#Provides a scripting component.
   """ Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable
        b: The b output variable
        c: The c output variable
        d: The d output variable
        """
        
import Rhino.Geometry as rg

#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
#output the vectors to a

a = []
numberfaces =  len(m.Faces)
for i in range(numberfaces):
    normals = m.FaceNormals[i]
    reversesn = rg.Vector3d.Negate(normals)
    a.append(reversesn)


#2.
#get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
#store the centers into a list called centers 
#output that list to b

b = []
for i in range(numberfaces):
    face = m.Faces.GetFaceCenter(i)
    b.append(face)


#b = centers

#3.
#calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
#store the angles in a list called angleList and output it to c

#c = angleList

c = []
for i in range(numberfaces):
    angle = rg.Vector3d.VectorAngle(a[i],s)
    c.append(angle)


#4. explode the mesh - convert each face of the mesh into a mesh
#for this, you have to first copy the mesh using rg.Mesh.Duplicate()
#then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
#and store the result into a list called exploded in output d

#d = explodedmesh

explodedmesh = []
novo = len(rg.Mesh.Duplicate(m).Faces)
m_novo = m.Duplicate()
for i in range(novo):
    face_mesh = m_novo.Faces.ExtractFaces([0])
    explodedmesh.append(face_mesh)

d = explodedmesh

f = novo

#after here, your task is to apply a transformation to each face of the mesh
#the transformation should correspond to the angle value that corresponds that face to it... 
#the result should be a mesh that responds to the sun position... its up to you!
