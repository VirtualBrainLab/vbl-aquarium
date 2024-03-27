using UnityEngine;

public struct AtlasModel
{
    public string Name;
    public Vector3 ReferenceCoord;
    public StructureModel[] Areas;
    public string Colormap;
}


public struct CameraModel
{
    public float Id;
    public string Type;
    public Vector3 Position;
    public Vector3 Rotation;
    public Vector3 Target;
    public float Zoom;
    public Vector2 Pan;
    public CameraMode Mode;
    public bool Controllable;
    public bool Main;
}


public enum CameraMode
{
    orthographic = 0,
    perspective = 1,
}


public struct CustomAtlasModel
{
    public string Name;
    public Vector3 Dimensions;
    public Vector3 Resolution;
}


public struct CustomMeshData
{
    public string ID;
    public Vector3[] Vertices;
    public int[] Triangles;
    public Vector3[] Normals;
}


public struct CustomMeshModel
{
    public string ID;
    public Vector3 Position;
    public bool UseReference;
    public string Material;
    public Vector3 Scale;
    public Color Color;
}


public struct MeshModel
{
    public string ID;
    public string Shape;
    public Vector3 Position;
    public Color Color;
    public Vector3 Scale;
    public string Material;
    public bool Interactive;
}


public struct ParticleGroupModel
{
    public string ID;
    public Vector3 Scale;
    public string Shape;
    public string Material;
    public float[] Xs;
    public float[] Ys;
    public float[] Zs;
    public Color[] Colors;
}

public struct PrimitiveMeshModel
{
    public MeshModel[] Data;
}


public struct StructureModel
{
    public string Name;
    public string Acronym;
    public int AtlasId;
    public Color Color;
    public bool Visible;
    public float ColorIntensity;
    public int Side;
    public string Material;
}

