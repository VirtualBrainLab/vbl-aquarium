using UnityEngine;
using System;

[Serializable]
public struct AffineTransformModel
{
    public Vector3 Scaling;
    public Vector3 Rotation;

    public AffineTransformModel(Vector3 scaling, Vector3 rotation)
    {
        Scaling = scaling;
        Rotation = rotation;
    }
}

[Serializable]
public struct CraniotomyGroup
{
    public string Atlas;
    public CraniotomyModel[] Data;

    public CraniotomyGroup(string atlas, CraniotomyModel[] data)
    {
        Atlas = atlas;
        Data = data;
    }
}


[Serializable]
public struct CraniotomyModel
{
    public int Index;
    public Vector2 Size;
    public Vector3 Position;
    public bool Rectangle;

    public CraniotomyModel(int index, Vector2 size, Vector3 position, bool rectangle)
    {
        Index = index;
        Size = size;
        Position = position;
        Rectangle = rectangle;
    }
}

