// Automatic FlutterFlow imports
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/custom_code/widgets/index.dart'; // Imports other custom widgets
import '/flutter_flow/custom_functions.dart'; // Imports custom functions
import 'package:flutter/material.dart';

import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart' as ll;

class DynamicMap extends StatefulWidget {
  const DynamicMap({
    super.key,
    this.width,
    this.height,
    this.points,
    required this.accessToken,
    required this.startingPoint,
    required this.startingZoom,
  });

  final double? width;
  final double? height;
  final List<LatLng>? points;
  final String accessToken;
  final LatLng startingPoint;
  final double startingZoom;

  @override
  State<DynamicMap> createState() => _DynamicMapState();
}

class _DynamicMapState extends State<DynamicMap> {
  List<Marker> allMarkers = [];

  @override
  void initState() {
    super.initState();
    addMarkersToMap(widget.points);
  }

  void addMarkersToMap(List<LatLng>? points) {
    for (LatLng point in points!) {
      allMarkers.add(
        Marker(
          point: ll.LatLng(point.latitude, point.longitude),
          height: 12,
          width: 12,
          builder: (BuildContext ctx) => Icon(
            Icons.location_pin,
            color: Colors.red,
          ),
          anchorPos: AnchorPos.exactly(Anchor(0, -12)),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return FlutterMap(
      options: MapOptions(
        center: ll.LatLng(
            widget.startingPoint.latitude, widget.startingPoint.longitude),
        zoom: widget.startingZoom,
      ),
      children: [
        TileLayer(
          urlTemplate:
              'MAPBOX API URL GOES HERE',
        ),
        MarkerLayer(
          markers: allMarkers,
        ),
      ],
    );
  }
}