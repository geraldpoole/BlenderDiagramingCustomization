{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import bpy\
\
def apply_modifiers(obj):\
     ctx = bpy.context.copy()\
     ctx['object'] = obj\
     for _, m in enumerate(obj.modifiers):\
         try:\
             ctx['modifier'] = m\
             bpy.ops.object.modifier_apply(ctx, modifier=m.name)\
         except RuntimeError:\
             print(f"Error applying \{m.name\} to \{obj.name\}, removing it instead.")\
             obj.modifiers.remove(m)\
             \
for o in bpy.data.objects:\
     apply_modifiers(o)}