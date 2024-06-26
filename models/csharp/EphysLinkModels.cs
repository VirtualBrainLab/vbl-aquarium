using UnityEngine;
using System;

[Serializable]
public struct AngularResponse
{
    public Vector3 Angles;
    public string Error;

    public AngularResponse(Vector3 angles, string error)
    {
        Angles = angles;
        Error = error;
    }
}

[Serializable]
public struct BooleanStateResponse
{
    public bool State;
    public string Error;

    public BooleanStateResponse(bool state, string error)
    {
        State = state;
        Error = error;
    }
}

[Serializable]
public struct CanWriteRequest
{
    public string ManipulatorId;
    public bool CanWrite;
    public float Hours;

    public CanWriteRequest(string manipulatorId, bool canWrite, float hours)
    {
        ManipulatorId = manipulatorId;
        CanWrite = canWrite;
        Hours = hours;
    }
}

[Serializable]
public struct DriveToDepthRequest
{
    public string ManipulatorId;
    public float Depth;
    public float Speed;

    public DriveToDepthRequest(string manipulatorId, float depth, float speed)
    {
        ManipulatorId = manipulatorId;
        Depth = depth;
        Speed = speed;
    }
}

[Serializable]
public struct DriveToDepthResponse
{
    public float Depth;
    public string Error;

    public DriveToDepthResponse(float depth, string error)
    {
        Depth = depth;
        Error = error;
    }
}

[Serializable]
public struct EphysLinkOptions
{
    public bool Background;
    public bool IgnoreUpdates;
    public string Type;
    public bool Debug;
    public bool UseProxy;
    public string ProxyAddress;
    public int Port;
    public int MpmPort;
    public string Serial;

    public EphysLinkOptions(bool background, bool ignoreUpdates, string type, bool debug, bool useProxy, string proxyAddress, int port, int mpmPort, string serial)
    {
        Background = background;
        IgnoreUpdates = ignoreUpdates;
        Type = type;
        Debug = debug;
        UseProxy = useProxy;
        ProxyAddress = proxyAddress;
        Port = port;
        MpmPort = mpmPort;
        Serial = serial;
    }
}


[Serializable]
public struct GetManipulatorsResponse
{
    public string[] Manipulators;
    public int NumAxes;
    public Vector4 Dimensions;
    public string Error;

    public GetManipulatorsResponse(string[] manipulators, int numAxes, Vector4 dimensions, string error)
    {
        Manipulators = manipulators;
        NumAxes = numAxes;
        Dimensions = dimensions;
        Error = error;
    }
}


[Serializable]
public struct GotoPositionRequest
{
    public string ManipulatorId;
    public Vector4 Position;
    public float Speed;

    public GotoPositionRequest(string manipulatorId, Vector4 position, float speed)
    {
        ManipulatorId = manipulatorId;
        Position = position;
        Speed = speed;
    }
}

[Serializable]
public struct InsideBrainRequest
{
    public string ManipulatorId;
    public bool Inside;

    public InsideBrainRequest(string manipulatorId, bool inside)
    {
        ManipulatorId = manipulatorId;
        Inside = inside;
    }
}


[Serializable]
public struct PositionalResponse
{
    public Vector4 Position;
    public string Error;

    public PositionalResponse(Vector4 position, string error)
    {
        Position = position;
        Error = error;
    }
}

[Serializable]
public struct ShankCountResponse
{
    public int ShankCount;
    public string Error;

    public ShankCountResponse(int shankCount, string error)
    {
        ShankCount = shankCount;
        Error = error;
    }
}

