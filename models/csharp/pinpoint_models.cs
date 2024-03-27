using UnityEngine;



public struct CraniotomyGroup
{
    public string Atlas;
    public CraniotomyModel[] Data;
}





public struct CraniotomyModel
{
    public int Index;
    public Vector2 Size;
    public Vector3 Position;
    public bool Rectangle;
}


